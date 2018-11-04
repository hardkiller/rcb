const elixir = require('laravel-elixir');

require('laravel-elixir-vue-2');

elixir((mix) => {
    mix.sass('app.scss')
    .copy('node_modules/font-awesome/fonts', 'public/fonts')
    .copy('node_modules/leaflet/dist/images', 'public/css/images')
    .webpack('app.js');
});
