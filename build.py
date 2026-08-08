import os
import shutil
from pathlib import Path

from app import BASE_URL, PAGES, SUPPORTED_LANGUAGES, app, localized_path
from price_guide import PRICE_GUIDES


BUILD_DIR = Path("build")


def clean_build_dir() -> None:
    """
    清空并重新创建构建输出目录。

    :return: None，无返回值
    """
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)


def clean_generated_text(text: str) -> str:
    """
    清理生成文本中的行尾空格并保留文件结尾换行。

    :param text: 原始生成文本
    :return: str，清理后的文本
    """
    return "\n".join(line.rstrip() for line in text.splitlines()) + "\n"


def favicon_bytes() -> bytes:
    """
    生成一个简单的 16x16 ICO 图标文件内容。

    :return: bytes，ICO 二进制内容
    """
    width = 16
    height = 16
    pixel_data = bytes((112, 210, 118, 255) * width * height)
    mask_data = b"\x00" * (4 * height)
    dib_header = (
        (40).to_bytes(4, "little")
        + width.to_bytes(4, "little", signed=True)
        + (height * 2).to_bytes(4, "little", signed=True)
        + (1).to_bytes(2, "little")
        + (32).to_bytes(2, "little")
        + (0).to_bytes(4, "little")
        + len(pixel_data).to_bytes(4, "little")
        + (0).to_bytes(4, "little", signed=True)
        + (0).to_bytes(4, "little", signed=True)
        + (0).to_bytes(4, "little")
        + (0).to_bytes(4, "little")
    )
    image = dib_header + pixel_data + mask_data
    directory = (
        bytes([width, height, 0, 0])
        + (1).to_bytes(2, "little")
        + (32).to_bytes(2, "little")
        + len(image).to_bytes(4, "little")
        + (22).to_bytes(4, "little")
    )
    return b"\x00\x00\x01\x00\x01\x00" + directory + image


def save_route(path: str, html: str) -> None:
    """
    将路由 HTML 保存为 Cloudflare Pages 可发布的静态文件。

    :param path: 站内路由路径
    :param html: 渲染后的 HTML
    :return: None，无返回值
    """
    relative = path.strip("/")
    output_dir = BUILD_DIR / relative if relative else BUILD_DIR
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "index.html").write_text(clean_generated_text(html), encoding="utf-8")


def copy_static_assets() -> None:
    """
    复制静态资源到构建目录。

    :return: None，无返回值
    """
    files = [
        (Path("static/css/mistfall.css"), BUILD_DIR / "static/css/mistfall.css"),
        (Path("static/js/mistfall-planner.js"), BUILD_DIR / "static/js/mistfall-planner.js"),
    ]
    files.extend(
        (source, BUILD_DIR / "static/images" / source.name)
        for source in sorted(Path("static/images").glob("*.webp"))
    )
    for source, destination in files:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def write_root_files() -> None:
    """
    写入 robots、sitemap、llms、ads 和重定向文件。

    :return: None，无返回值
    """
    routes = []
    for page_key in PAGES:
        for locale in SUPPORTED_LANGUAGES:
            routes.append((page_key, localized_path(page_key, locale)))

    sitemap_urls = "\n".join(
        f"  <url><loc>{BASE_URL}{route.rstrip('/')}/</loc><lastmod>{PRICE_GUIDES['en']['checked_iso'] if page_key == 'price-guide' else '2026-07-31'}</lastmod></url>"
        for page_key, route in routes
    )
    (BUILD_DIR / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_urls}\n</urlset>\n',
        encoding="utf-8",
    )
    (BUILD_DIR / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}/sitemap.xml\n",
        encoding="utf-8",
    )
    (BUILD_DIR / "llms.txt").write_text(
        f"# Mistfall Loadouts\n\nIndependent Mistfall Hunter loadout planner, class guide, and build decision hub.\n\n- Homepage: {BASE_URL}/\n- Classes: {BASE_URL}/classes/\n- Builds: {BASE_URL}/builds/\n- Guide: {BASE_URL}/guide/\n- Price guide: {BASE_URL}/mistfall-hunter-price/\n- Contact: {BASE_URL}/contact/\n",
        encoding="utf-8",
    )
    (BUILD_DIR / "llms-full.txt").write_text(
        f"# Mistfall Loadouts Full Context\n\nMistfall Loadouts helps players choose launch-week Mistfall Hunter loadouts by class role, weapon style, risk tolerance, and extraction goal. The site labels assumptions clearly and avoids claiming official hidden values.\n\nCanonical domain: {BASE_URL}\nLast updated: 2026-07-31\n",
        encoding="utf-8",
    )
    (BUILD_DIR / "ads.txt").write_text(
        "google.com, pub-9042195580058659, DIRECT, f08c47fec0942fa0\n",
        encoding="utf-8",
    )
    (BUILD_DIR / "favicon.ico").write_bytes(favicon_bytes())
    redirects = [
        "/classes /classes/ 301",
        "/builds /builds/ 301",
        "/guide /guide/ 301",
        "/about /about/ 301",
        "/contact /contact/ 301",
        "/privacy-policy /privacy-policy/ 301",
        "/terms-of-service /terms-of-service/ 301",
    ]
    for locale in SUPPORTED_LANGUAGES:
        prefix = "" if locale == "en" else f"/{locale}"
        redirects.append(f"{prefix}/mistfall-hunter-price {prefix}/mistfall-hunter-price/ 301")
    (BUILD_DIR / "_redirects").write_text("\n".join(redirects) + "\n", encoding="utf-8")
    (BUILD_DIR / "_worker.js").write_text(
        "export default {\n"
        "  async fetch(request, env) {\n"
        "    const url = new URL(request.url);\n"
        "    if (url.hostname === 'www.mistfallloadouts.blog') {\n"
        "      url.hostname = 'mistfallloadouts.blog';\n"
        "      return Response.redirect(url.toString(), 301);\n"
        "    }\n"
        "    return env.ASSETS.fetch(request);\n"
        "  }\n"
        "};\n",
        encoding="utf-8",
    )


def build_site() -> None:
    """
    渲染并导出整个静态站点。

    :return: None，无返回值
    """
    clean_build_dir()
    with app.test_client() as client:
        for page_key in PAGES:
            for locale in SUPPORTED_LANGUAGES:
                route = localized_path(page_key, locale)
                response = client.get(route)
                if response.status_code != 200:
                    raise RuntimeError(f"Build failed for {route}: {response.status_code}")
                save_route(route, response.data.decode("utf-8"))
        response = client.get("/missing-page/")
        (BUILD_DIR / "404.html").write_text(clean_generated_text(response.data.decode("utf-8")), encoding="utf-8")
    copy_static_assets()
    write_root_files()


if __name__ == "__main__":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    build_site()
