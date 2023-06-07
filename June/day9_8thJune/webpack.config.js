const path = require('path');

module.export = {
    entry: './src/index.js',  // this defines the entry point of your application
    output: {
        filename: 'awesome.js',
        path: path.resolve(__dirname, 'dist'),
    }
};