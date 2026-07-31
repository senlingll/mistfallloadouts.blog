import os
import shutil
from pathlib import Path

from app import BASE_URL, PAGES, SUPPORTED_LANGUAGES, app, localized_path


BUILD_DIR = Path("build")


def clean_build_dir() -> None:
    """
    清空并重新创建构建输出目录。

    :return: None，无返回值
    """
    if BUILD_DIR.exists():
        shutil.rmtree(BUILD_DIR)
    BUILD_DIR.mkdir(parents=True, exist_ok=True)


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
    (output_dir / "index.html").write_text(html, encoding="utf-8")


def copy_static_assets() -> None:
    """
    复制静态资源到构建目录。

    :return: None，无返回值
    """
    files = [
        (Path("static/css/mistfall.css"), BUILD_DIR / "static/css/mistfall.css"),
        (Path("static/js/mistfall-planner.js"), BUILD_DIR / "static/js/mistfall-planner.js"),
    ]
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
            routes.append(localized_path(page_key, locale))

    sitemap_urls = "\n".join(
        f"  <url><loc>{BASE_URL}{route.rstrip('/')}/</loc><lastmod>2026-07-31</lastmod></url>" for route in routes
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
        f"# Mistfall Loadouts\n\nIndependent Mistfall Hunter loadout planner, class guide, and build decision hub.\n\n- Homepage: {BASE_URL}/\n- Classes: {BASE_URL}/classes/\n- Builds: {BASE_URL}/builds/\n- Guide: {BASE_URL}/guide/\n- Contact: {BASE_URL}/contact/\n",
        encoding="utf-8",
    )
    (BUILD_DIR / "llms-full.txt").write_text(
        f"# Mistfall Loadouts Full Context\n\nMistfall Loadouts helps players choose launch-week Mistfall Hunter loadouts by class role, weapon style, risk tolerance, and extraction goal. The site labels assumptions clearly and avoids claiming official hidden values.\n\nCanonical domain: {BASE_URL}\nLast updated: 2026-07-31\n",
        encoding="utf-8",
    )
    (BUILD_DIR / "ads.txt").write_text("", encoding="utf-8")
    (BUILD_DIR / "_redirects").write_text(
        "/classes /classes/ 301\n/builds /builds/ 301\n/guide /guide/ 301\n/about /about/ 301\n/contact /contact/ 301\n/privacy-policy /privacy-policy/ 301\n/terms-of-service /terms-of-service/ 301\n",
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
        (BUILD_DIR / "404.html").write_text(response.data.decode("utf-8"), encoding="utf-8")
    copy_static_assets()
    write_root_files()


if __name__ == "__main__":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    build_site()
