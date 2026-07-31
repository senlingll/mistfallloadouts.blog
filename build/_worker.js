export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === 'www.mistfallloadouts.blog') {
      url.hostname = 'mistfallloadouts.blog';
      return Response.redirect(url.toString(), 301);
    }
    return env.ASSETS.fetch(request);
  }
};
