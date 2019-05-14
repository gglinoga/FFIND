import React from 'react'
import {
  Container,
  Row,
  Col
} from 'reactstrap'

import MetaTags from 'react-meta-tags'

import TeamMember from './TeamMember'
import MapPicture from './assets/map-collaborations6.png'

export default class Collaborators extends React.Component {
  render () {
    return (
      <div className='collaborators'>
        <MetaTags>
          <title>Collaborators -- Pancreatlas / HANDEL-P</title>
          <meta name='description' content='Who is working together to create the HANDEL-P project?' />
        </MetaTags>
        {/* <Header heading="Collaborators" subheading="Creating multi-disciplinary expert groups" /> */}
        <Container fluid>
          <Container>
            <Row className='v-padded'>
              <Col md='6'>
                <h1>Creating Connections</h1>
                <p>We are cross-pollinating numerous activities and programs to develop new ideas that accelerate diabetes research, education and clinical care.</p>
                <p>If you are interested in collaborating with us&mdash;eitheer by accessing tissue samples or contributing images&mdash;pease get in touch!</p>
              </Col>
              <Col md='6'>
                <img src={MapPicture} alt='Collaborators map' className='img-fill' />
              </Col>
            </Row>
          </Container>
        </Container>

        <Container fluid className='shaded'>

          <Container className='v-padded'>
            <h2><span>Meet the investigators</span></h2>
            <Row className='mt-2'>
              <Col md='4'>
                <TeamMember name='Mark Atkinson' institution='University of Florida' desc='Our laboratory seeks to directly define methods for disease prevention in non-diabetic subjects identified to be at increased risk for the disease or diabetic subjects through pancreatic transplantation in association with novel forms of immunotherapy.' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/mark-atkinson.jpg' site='https://diabetes.ufl.edu/atkinson-lab/' email='mailto:atkinson@pathology.ufl.edu' phone='tel:352-273-8277' />
              </Col>
              <Col md='4'>
                <TeamMember name='Rita Bottino' institution='Allegheny General Hospital, Pittsburgh' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/rita-bottino.jpg' site='https://www.ahn.org/research/our-research-institutes/cellular-therapeutics/our-team' email='mailto:rita.bottino@ahn.org' phone='tel:412-512-6496' desc='Our team is a reference laboratory for the isolation and distribution is islets of Langerhans obtained from the pancreas of deceased organ donors for research purposes' />
              </Col>
              <Col md='4'>
                <TeamMember name='Marcela Brissova' institution='Vanderbilt University Medical Center' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/marcela-brissova.jpg' site='https://medicine.mc.vanderbilt.edu/person/marcela-brissova-phd' email='mailto:marcela.brissova@vanderbilt.edu' phone='tel:615-936-1729' desc='Our research interests include the biology of pancreatic islets with a focus on the regulation of beta cell gene expression to provide insight into processes controlling normal pancreatic beta cell function in rodent models and translating this research to human islet biology.' />
              </Col>
            </Row>
            <Row className='mt-2'>
              <Col md='4'>
                <TeamMember name='Chunhua Dai' institution='Vanderbilt University Medical Center' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/chunhua-dai.jpg' site='https://www.powersresearch.org/people' email='mailto:chunhua.dai@vanderbilt.edu' phone='tel:615-936-7678' desc='Our research is focused on the molecular, cellular, and vascular changes in human islets when they are challenged with hyperglycemia and/or insulin resistance in vivo.' />
              </Col>
              <Col md='4'>
                <TeamMember name='Seung Kim' institution='Stanford University' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/seung-kim.jpg' site='https://seungkimlab.stanford.edu/' email='mailto:seungkim@stanford.edu' phone='tel:650-723-6230' desc='The Kim lab studies islet and pancreas biology with the aim of developing diagnostic and therapeutic paradigms for human diseases.' />
              </Col>
              <Col md='4'>
                <TeamMember name='Al Powers' institution='Vanderbilt University Medical Center' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/al-powers.jpg' site='https://www.powersresearch.org/' email='mailto:al.powers@vanderbilt.edu' phone='tel:615-936-7678' desc='The Powers lab seeks to understand and reverse β-cell and islet abnormalities and dysfunction in type 1 and type 2 diabetes.' />
              </Col>
            </Row>
            <Row className='mt-2'>
              <Col md='4'>
                <TeamMember name='Chris Wright' institution='Vanderbilt University Medical Center' imgSrc='https://dev8-labnodes.app.vanderbilt.edu/assets/handelp/media/chris-wright.jpg' site='https://lab.vanderbilt.edu/wright-lab/' email='mailto:chris.wright@vanderbilt.Edu' phone='tel:615-343-8256' desc='The Wright lab focuses on early embryonic development and organogenesis.' />
              </Col>
            </Row>
          </Container>
        </Container>

      </div>
    )
  }
}
