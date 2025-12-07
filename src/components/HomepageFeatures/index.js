import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Easy to Use',
    Svg: '/img/logo.jpg', // static path
    description: (
      <>Quickly set up your website and start publishing your content easily.</>
    ),
  },
  {
    title: 'Focus on What Matters',
    Svg: '/img/mogo.jpg',
    description: (
      <>Focus on your course content, Docusaurus takes care of the rest.</>
    ),
  },
  {
    title: 'Powered by React',
    Svg: '/img/pogo.jpg',
    description: (
      <>Customize layouts and extend components using React components.</>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <img className={styles.featureSvg} src={Svg} alt={title} />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
