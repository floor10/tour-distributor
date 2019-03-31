import * as React from "react";
import * as ReactDOM from "react-dom";
import TextField from '@material-ui/core/TextField';
import FormGroup from '@material-ui/core/FormGroup';

export default (props) => (
    <FormGroup>
        <TextField
            id="outlined-search"
            label="Табельный номер"
            type="search"
            margin="dense"
            variant="outlined"
        >
        </TextField>
    </FormGroup>);