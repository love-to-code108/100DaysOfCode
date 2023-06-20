const path = require('path');
// const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
// const bundleAnalyzer = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    mode: "development",
    entry: './src/index.js',  // this defines the entry point of your application or basically like your source files
    output: {
        path: path.resolve(__dirname, 'dist'),   // basically like your output file 
        filename: 'awesome.js',                  // file name of the output file
    },
    module:{
        rules:[
            {
                test: /\.css$/,
                use:[
                    'style-loader',
                    'css-loader',
                ],
            },
        ],
    },
    // plugins: [
    //     new BundleAnalyzerPlugin()      
    // ]
};