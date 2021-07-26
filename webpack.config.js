const path = require("path")
const MiniCssExtractPlugin = require("mini-css-extract-plugin")

module.exports = {
  // entry: './assets/index.js',  // path to our input file
  entry: {
    global: ["./assets/js/index.js"],
    singlemap: ["./assets/js/singlemap.js", "./assets/js/drawFlight.js"],
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
          name: "img/[name]_[hash:7].[ext]",
        },
      }],
    }],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "css/style-[name].css",
    }),
  ],
}
