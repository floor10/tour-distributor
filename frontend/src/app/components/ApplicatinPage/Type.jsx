import * as React from "react";
import * as ReactDOM from "react-dom";
import FormControl from '@material-ui/core/FormControl';
import FormLabel from '@material-ui/core/FormLabel';
import RadioGroup from '@material-ui/core/RadioGroup';
import Radio from '@material-ui/core/Radio';
import FormControlLabel from '@material-ui/core/FormControlLabel';

let value = 1;
const handleChange = (newValue) => {
    value = newValue
}

export default class Type extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            value: 'family'
        }
    }
    handleChange = event => {
        this.setState({ value: event.target.value });
      };

    render() {
        return (<FormControl component="fieldset">
        {/* <FormLabel component="legend">Тип заявки</FormLabel> */}
        <RadioGroup
          aria-label="Тип заявки"
          name="application_type"
          value={this.state.value}
          onChange={this.handleChange}
        >
          <FormControlLabel value="family" control={<Radio />} label="Семейная" />
          <FormControlLabel value="children" control={<Radio />} label="Детские" />

        </RadioGroup>
      </FormControl>);
    }
}