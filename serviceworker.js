var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
    '/',
     '/formulario/',
    // 'https://fonts.googleapis.com/css?family=Codystar', FUENTE QUE NO SE MUESTRA
    '/static/core/css/estilos.css',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.css',
    'https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js',
    'https://cdn.jsdelivr.net/bxslider/4.2.12/jquery.bxslider.min.js',
    '/static/core/img/social-twitter.png',
    '/static/core/img/socialfacebook.png',
    '/static/core/img/social-inst.png',
    '/static/core/img/logo.png',
    '/static/core/img/rescate.jpg',
    '/static/core/img/crowfunding.jpg',
    '/static/core/img/socialplus.png',
    '/static/core/img/perro.png',
    '/static/core/img/google-plus1.png',
    '/static/core/img/Email.png',
    '/static/core/img/Facebook.png',
    '/static/core/img/Apolo.jpg',
    '/static/core/img/Bigotes.jpg',
    '/static/core/img/Chocolate.jpg',
    '/static/core/img/Duque.jpg',
    '/static/core/img/Luna.jpg',
    '/static/core/img/Pexel.jpg',
    '/static/core/img/Tom2.jpg',
    '/static/core/img/Wifi.jpg',
    '/static/core/img/instagram.png',
    '/static/core/img/Maya.jpg',
    '/static/core/img/Oso.jpg',
    
];



self.addEventListener('install', function(event) {
  // Perform install steps
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});

self.addEventListener('fetch', function(event){
    event.respondWith(
        caches.match(event.request).then(function(response) {
           
            
            return fetch(event.request).catch(function() {
                console.log("no funciona")
                return response;
            });
        })
    );

});


importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');

var config = {
    apiKey: "AIzaSyAcSnus64ABaMK8ojQW0JzOYcDKdll74Oc",
    authDomain: "misperris-2346e.firebaseapp.com",
    databaseURL: "https://misperris-2346e.firebaseio.com",
    projectId: "misperris-2346e",
    storageBucket: "misperris-2346e.appspot.com",
    messagingSenderId: "766826330646"
};
firebase.initializeApp(config);

const messaging = firebase.messaging();

//Programamos una funcion que estara escuchando cuando llegue una notificacion desde Firebase

messaging.setBackgroundMessageHandler(function(){
    //El playload contendra el mensaje destinado al usuario
    var title = "Notificacion"
    var options = {
        body:"Este es el cuerpo del mensaje"
    }

    //Mostramos la notificacion al usuario
    return self.registration.showNotification(title, options);

})
