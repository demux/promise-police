const path = require('path')
const webpack = require('webpack')
const BundleTracker = require('webpack-bundle-tracker')


module.exports = {
  context: __dirname,
  entry: './assets/js/main.js',
  output: {
      path: path.resolve('./assets/webpack_bundles/'),
      filename: "[name]-[hash].js"
  },
  module: {
    loaders: [{
      test: /\.js$/,
      exclude: /node_modules/,
      loader: 'babel'
    }, {
      test: /\.json$/,
      loader: 'json'
    }],
    noParse: /\.min\.js/
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
}
