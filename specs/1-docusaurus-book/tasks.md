# Tasks: Physical AI & Humanoid Robotics Course Book with Docusaurus

**Feature Branch**: `1-docusaurus-book`
**Created**: 2025-12-04
**Plan**: [specs/1-docusaurus-book/plan.md](specs/1-docusaurus-book/plan.md)

## Ordered Tasks

1.  **Set up Docusaurus project**: Initialize a new Docusaurus project in the repository root using the Docusaurus CLI (`npx create-docusaurus@latest . classic`).
2.  **Configure `docusaurus.config.js`**: Update the Docusaurus configuration file (`docusaurus.config.js`) with project metadata (title: "Physical AI & Humanoid Robotics Course", description: "A comprehensive course on Physical AI and Humanoid Robotics.", author: "Claude Code") and initial deployment settings for GitHub Pages (`baseUrl`, `projectName`, `organizationName`).
3.  **Create `docs/` folder and chapter directories**: Create the `docs/` directory if it doesn't exist and create subdirectories for each of the 5 chapters (`docs/chapter1/`, `docs/chapter2/`, `docs/chapter3/`, `docs/chapter4/`, `docs/chapter5/`).
4.  **Create initial chapter Markdown files**: For each chapter (1-5), create an `index.md` file within its respective `docs/chapterN/` directory. Include Docusaurus front matter (e.g., `id: chapter1`, `title: Chapter 1: Introduction to Physical AI`).
5.  **Create `sidebars.js`**: Define the `sidebars.js` file to include all 5 chapters in the correct order for navigation within the `tutorialSidebar` array.
6.  **Outline Chapter 1 lessons**: Add lesson subheadings (`## Lesson Title`) and placeholder content to `docs/chapter1/index.md`.
7.  **Outline Chapter 2 lessons**: Add lesson subheadings (`## Lesson Title`) and placeholder content to `docs/chapter2/index.md`.
8.  **Outline Chapter 3 lessons**: Add lesson subheadings (`## Lesson Title`) and placeholder content to `docs/chapter3/index.md`.
9.  **Outline Chapter 4 lessons**: Add lesson subheadings (`## Lesson Title`) and placeholder content to `docs/chapter4/index.md`.
10. **Outline Chapter 5 lessons**: Add lesson subheadings (`## Lesson Title`) and placeholder content to `docs/chapter5/index.md`.
11. **Install Docusaurus dependencies**: Run `npm install` (or `yarn install`) in the project root to install all necessary Docusaurus project dependencies.
12. **Local preview and testing**: Start the Docusaurus development server (`npm start` or `yarn start`) and thoroughly verify the site structure, navigation, and content rendering of all chapters and lessons locally.
13. **Build Docusaurus site**: Build the Docusaurus site for production (`npm run build` or `yarn build`) to generate static assets.
14. **Deploy to GitHub Pages**: Follow Docusaurus-specific instructions to deploy the built static site to GitHub Pages, ensuring public accessibility.
15. **Document process for adding future chapters**: Ensure the `plan.md` (or a dedicated section in `tasks.md` if more appropriate) clearly outlines the steps for adding new chapters, including creating markdown files, updating `sidebars.js`, and leveraging AI for content generation.
