const path = require('path');

module.exports = {
    mode: "development",
    entry: './src/index.js',  // this defines the entry point of your application
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'awesome.js',
    }
};