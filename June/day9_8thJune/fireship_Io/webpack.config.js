const path = require('path');
const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
const bundleAnalyzer = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    mode: "development",
    entry: './src/index.js',  // this defines the entry point of your application
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'awesome.js',
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
    plugins: [
        new BundleAnalyzerPlugin()      
    ]
};