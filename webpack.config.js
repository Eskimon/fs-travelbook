const path = require("path")
const MiniCssExtractPlugin = require("mini-css-extract-plugin")
const Webpack = require("webpack")
const { CleanWebpackPlugin } = require("clean-webpack-plugin")
const CopyWebpackPlugin = require("copy-webpack-plugin")
const HtmlWebpackPlugin = require("html-webpack-plugin")
const BundleTracker = require("webpack-bundle-tracker")

module.exports = {
  mode: "development",
  entry: {
    global: ["./assets/js/index.js", "./assets/js/drawFlight.js", "./assets/js/drawPicture.js"],
  },
  output: {
    filename: "js/bundle-[name].js",  // output bundle file name
    path: path.resolve(__dirname, "./static"),  // path to our Django static directory
  },
  module: {
    rules: [{
      test: /\.scss$/,
      use: [
        MiniCssExtractPlugin.loader,
        {
          loader: "css-loader",
        },
        {
          loader: "sass-loader",
          options: {
            sourceMap: true,
            // options...
          },
        },
      ],
    }, {
      test: /\.css$/,
      use: [
        "style-loader",
        "css-loader",
      ],
    },
    {
      test: /\.(png|svg|jpg|gif)$/,
      use: [{
        loader: "file-loader",
        options: {
          name: "img/[name].[ext]",
        },
      }],
    }],
  },
  plugins: [
    // new CleanWebpackPlugin(),
    // new CopyWebpackPlugin({ patterns: [{ from: path.resolve(__dirname, '../public'), to: 'public' }] }),
    // new HtmlWebpackPlugin({
    //   template: path.resolve(__dirname, '../src/index.html'),
    // }),
    new BundleTracker({filename: "./webpack-stats.json"}),
    new Webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("development"),
    }),
    new MiniCssExtractPlugin({
      filename: "css/style-[name].css",
    }),
  ],
}
