// vue.config.js

/**
 * @type {import('@vue/cli-service').ProjectOptions}
 */
 module.exports = {
    pages: {
        index: {
          // entry for the page
          entry: 'src/pages/Home/main.js',
          // the source template
          template: 'public/index.html',
          // output as dist/index.html
        //   filename: 'index.html',
          // when using title option,
          // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
          title: 'Home',
          // chunks to include on this page, by default includes
          // extracted common chunks and vendor chunks.
        //   chunks: ['chunk-vendors', 'chunk-common', 'index']
        },
        resume: {
            // entry for the page
            entry: 'src/pages/Resume/resume.js',
            // the source template
            template: 'public/index.html',
            // output as dist/index.html
            // filename: 'resume.html',
            // when using title option,
            // template title tag needs to be <title><%= htmlWebpackPlugin.options.title %></title>
            title: 'Resume',
            // chunks to include on this page, by default includes
            // extracted common chunks and vendor chunks.
            // chunks: ['chunk-vendors', 'chunk-common', 'index']
          },
        // when using the entry-only string format,
        // template is inferred to be `public/subpage.html`
        // and falls back to `public/index.html` if not found.
        // Output filename is inferred to be `subpage.html`.
        // subpage: 'src/subpage/main.js'
      }
  }