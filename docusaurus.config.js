// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics Course',
  tagline: 'A comprehensive course on Physical AI and Humanoid Robotics',
  

  // Works locally + works after deployment
  favicon: '/img/favicon.png',

  future: {
    v4: true,
  },

  // LOCAL DEVELOPMENT → keep these 2 values like this:
  url: 'http://localhost:3000',
  baseUrl: '/',

  // When you deploy to GitHub Pages, change these 2:
  // url: 'https://your-github-username.github.io',
  // baseUrl: '/physical-ai-book/',

  organizationName: 'your-github-username',
  projectName: 'physical-ai-book',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://localhost:3000',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/your-github-username/physical-ai-book/edit/main/blog/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig: {
    image: '/img/social.jpg',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: true,
    },

    navbar: {
      title: 'Physical AI & Humanoid Robotics Course',
      logo: {
        alt: 'Physical AI Logo',
        src: '/img/favicon.png',
      },
      items: [
      {
  type: 'docSidebar',
  sidebarId: 'tutorialSidebar',
  position: 'left',
  label: 'Course',
}

     
      ],
    },

    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [{ label: 'Tutorial', to: '/docs/chapter1/index' }],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            { label: 'Discord', href: 'https://discord.com/invite/docusaurus' },
            { label: 'X', href: 'https://x.com/docusaurus' },
           ],
        },
        {
          title: 'More',
          items: [
            { label: 'Blog', to: '/blog' },
            {
              label: 'GitHub',
              href: 'https://github.com/your-github-username/physical-ai-book',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI Course. Built with Docusaurus.`,
    },

    prism: {
      theme: prismThemes.vsLight,
      darkTheme: prismThemes.vsDark,
    },
  },
};

export default config;
