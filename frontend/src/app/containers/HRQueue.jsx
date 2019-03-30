import * as React from "react";
import * as ReactDOM from "react-dom";
import { withStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import FormGroup from '@material-ui/core/FormGroup';
import Button from '@material-ui/core/Button';
import QueueTable from '../components/QueueTable';

const styles = theme => ({
    root: {
        flexGrow: 1,
    },
    paper: {
        padding: theme.spacing.unit * 2,
        textAlign: 'center',
        color: theme.palette.text.secondary,
    },
});

let id = 0;
function createData(name, calories, fat, carbs, protein) {
    id += 1;
    return { id, name, calories, fat, carbs, protein };
}
const rows = [
    createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
    createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
    createData('Eclair', 262, 16.0, 24, 6.0),
    createData('Cupcake', 305, 3.7, 67, 4.3),
    createData('Gingerbread', 356, 16.0, 49, 3.9),
];
class Queue extends React.Component {
    render() {
        return (
            <div>
                <FormGroup>
                    <Button variant="contained" color="primary">
                        Export
                    </Button>
                </FormGroup>
                <FormGroup>
                    <TextField
                        id="outlined-search"
                        label="Search"
                        type="search"
                        margin="dense"
                        variant="outlined"
                    >
                    </TextField>
                </FormGroup>
                <div style={{ height: 30 }} />
                <QueueTable rows={rows} />
            </div>);
    }
}

export default withStyles(styles)(Queue);