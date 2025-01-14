/**
   * @author Jimmy Messmer
 */

import React from 'react'
import FilterItem from './FilterItem'

import {
  Row,
  Col,
  Input,
  Form,
  FormGroup
} from 'reactstrap'

// import { Range } from 'rc-slider'
import InputRange from 'react-input-range'

import 'react-input-range/lib/css/index.css'

/**
 * React component for a checkbox. This one is pretty simple--just returns a checkbox for each tag prop
 * @category Filtering
 * @author Jimmy Messmer
 * @extends React.Component
 */
class CheckboxFilterList extends React.Component {
  constructor(props) {
    super(props)
    this.addFilter = this.addFilter.bind(this)
    this.state = {
      activeFilters: this.props.tags.filter(tag => tag.active).map(tag => tag.name)
    }
  }

  /**
   * Toggle a new filter--if it is currently activated, deactivate or vice versa.
   * @param {*} newFilter 
   */
  addFilter(newFilter) {
    let oldFilters = JSON.parse(JSON.stringify(this.state.activeFilters))
    let newFilters = []
    if (oldFilters.indexOf(newFilter) < 0) {
      oldFilters.push(newFilter)
      newFilters = oldFilters
    } else {
      newFilters = oldFilters.filter(val => val !== newFilter)
    }

    this.setState({
      activeFilters: newFilters
    })

    this.props.callback(newFilters, [newFilter])
  }

  render() {
    return (
      this.props.tags.map(tag => (
        <FilterItem defaultChecked={tag.active} clear={this.props.clear} key={tag.name} filterName={tag.name} filterQty={this.props.tags[tag]} callback={() => this.addFilter(tag.name)} />
      ))
    )
  }
}

/**
 * React component for a slider.
 * @class SliderFilterList
 * @category Filtering
 * @author Jimmy Messmer
 */
class SliderFilterList extends React.Component {
  constructor(props) {
    super(props)
    this.onSliderChange = this.onSliderChange.bind(this)
    this.onToggleChange = this.onToggleChange.bind(this)
    this.updateMarks = this.updateMarks.bind(this)
    let leftMark = 0
    let rightMark = this.props.tags.length - 1
    for (let i = 0; i < this.props.tags.length; i++) {
      if (this.props.tags[i].active) {
        leftMark = i
        break
      }
    }
    for (let i = this.props.tags.length - 1; i >= 0; i--) {
      if (this.props.tags[i].active) {
        rightMark = i
        break
      }
    }
    this.state = {
      value: {
        min: leftMark,
        max: rightMark
      },
      active: this.props.tags.filter(tag => tag.active).length > 0,
      cleared: false
    }
  }

  /**
   * Reset the filter if the entire set is toggled off
   * @param {*} prevProps Old props for component
   */
  componentDidUpdate(prevProps) {
    if (prevProps.hidden === false && this.props.hidden === true) {
      this.setState({
        value: {
          min: 0,
          max: this.props.tags.length - 1
        },
        active: false,
        cleared: false
      })
    }
    else if (this.props.onClear===false && this.state.active===true){
      this.setState({
        value: {
          min:0,
          max: this.props.tags.length - 1
        },
        active: false,
      })
    }
  }

  /**
   * Update the matches from the slider element when it is updated 
   * @param {array} args Array of arguments--first element is the minimum value, second the maximum
   */
  onSliderChange(newValue) {
    // We should be able to just get all the current filters outside of the current age group + the selected ages
    if (this.state.active) {
      let oldMatches = this.props.tags.slice(this.state.value.min, this.state.value.max + 1).map(match => match.name)

      // Make sure we don't have any out of bounds exceptions
      let min = Math.max(0, newValue.value.min)
      let max = Math.min(this.props.tags.length - 1, newValue.value.max)
      let matches = this.props.tags.slice(min, max.max + 1).map(match => match.name)
      let diff = []
      if (oldMatches.length > matches.length) {
        diff = oldMatches.filter(val => matches.indexOf(val) < 0)
      } else {
        diff = matches.filter(val => oldMatches.indexOf(val) < 0)
      }
      this.setState({
        value: { min: min, max: max }
      })
      this.props.callback(matches, diff)
    }
  }

  onToggleChange() {
    if (!this.state.active) {
      let matches = this.props.tags
      this.props.callback(matches.map(match => match.name), matches.map(match => match.name))
    } else {
      this.props.callback([], this.props.tags.slice(this.state.value.min, this.state.value.max + 1).map(tag => tag.name))
      this.setState({
        value: {
          min: 0,
          max: this.props.tags.length - 1
        }
      })
    }
    this.setState(prevState => ({
      active: !prevState.active
    }))
    console.log('toggle')
  }


  /**
   * Update min and max marks on the slider element
   * @param {array} args Array with new minimum and maximum values
   */
  updateMarks(args) {
    this.setState({
      min: args[0],
      max: args[1]
    })
  }

  render() {
    if (this.props.hidden) {
      return null
    } else {
      return (
        <div>
          <Row className='age-slider pancreatlas-row'>
            <Form style={{ minWidth: '14rem' }} inline>
              <FormGroup style={{ width: '100%' }}>
                <Col xs={2}>
                  <Input type='checkbox' checked={this.state.active} onChange={this.onToggleChange}/>
                </Col>
                <Col xs={10} className={!this.state.active ? 'greyed-out' : ''}>
                    <InputRange
                      formatLabel={value => `${this.props.tags[value]['name']}`}
                      maxValue={this.props.tags.length - 1}
                      minValue={0}
                      value={this.state.value}
                      onChange={value => this.onSliderChange({ value })} />
                </Col>
              </FormGroup>
            </Form>
          </Row>
        </div>
      )
    }
  }

}

export { CheckboxFilterList, SliderFilterList }