console.log('Hello from sw.js');

importScripts('https://storage.googleapis.com/workbox-cdn/releases/6.0.2/workbox-sw.js');

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);

  workbox.precaching.precacheAndRoute([
    {
      url: '/',
      revision: '1'
    },
    {
      url: '/projects',
      revision: '1'
    },

    {
      url: '/static/index.css',
      revision: '1'
    },
    {
      url: new RegExp('/projects/\\d+/test#todo_list$'),  // Matches /projects/{number}/test#todo_list
      revision: '1'
    },
    {
      url: new RegExp('/projects/\\d+/test#formQuantities$'),  // Matches /projects/{number}/test#todo_list
      revision: '1'
    },
    {
      url: new RegExp('/projects/\\d+/test#projectMaterials$'),  // Matches /projects/{number}/test#todo_list
      revision: '1'
    },
    {
      url: '/static/index.js',
      revision: '1'
    }
  ]);

  workbox.routing.registerRoute(
    /\.(?:js|css)$/,
    new workbox.strategies.StaleWhileRevalidate({
      cacheName: 'static-resources',
    })
  );

  workbox.routing.registerRoute(
    new RegExp('/projects$'),
    new workbox.strategies.NetworkFirst()
  );

  workbox.routing.registerRoute(
    new RegExp('/projects/\\d+/materials$'),
    new workbox.strategies.NetworkFirst()
  );

  workbox.routing.registerRoute(
    /\.(?:png|gif|jpg|jpeg|svg)$/,
    new workbox.strategies.CacheFirst({
      cacheName: 'images',
      plugins: [
        new workbox.cacheableResponse.CacheableResponsePlugin({ statuses: [0, 200] }),
      ],
    })
  );

  workbox.routing.registerRoute(
    new RegExp('https://fonts.(?:googleapis|gstatic).com/(.*)'),
    new workbox.strategies.CacheFirst({
      cacheName: 'googleapis',
    })
  );
} else {
  console.log(`Boo! Workbox didn't load 😬`);
}
