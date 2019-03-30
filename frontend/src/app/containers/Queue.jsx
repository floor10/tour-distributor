import * as React from "react";
import * as ReactDOM from "react-dom";
import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

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
                <Paper>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell align="right">№ очереди</TableCell>
                                <TableCell align="right">Табель</TableCell>
                                <TableCell align="right">ФИО</TableCell>
                                <TableCell align="right">Родитель одиночка</TableCell>
                                <TableCell align="right">Категория</TableCell>
                                <TableCell align="right">Корпоративные награды (последние 2 года)</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows.map((row, index) => (
                                <TableRow key={row.id}>
                                    <TableCell align="right">{index + 1}</TableCell>
                                    <TableCell align="right">{index * 5132 + 1213}</TableCell>
                                    <TableCell component="th" scope="row">
                                        {row.name}
                                    </TableCell>
                                    <TableCell align="right">{row.calories}</TableCell>
                                    <TableCell align="right">{row.fat}</TableCell>
                                    <TableCell align="right">{row.carbs}</TableCell>
                                    <TableCell align="right">{row.protein}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </Paper>
                <div style={{ height: 30 }} />
                <Paper>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell align="right">№ очереди</TableCell>
                                <TableCell align="right">Табель</TableCell>
                                <TableCell align="right">ФИО</TableCell>
                                <TableCell align="right">Родитель одиночка</TableCell>
                                <TableCell align="right">Категория</TableCell>
                                <TableCell align="right">Корпоративные награды (последние 2 года)</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                                <TableRow key={1023}>
                                    <TableCell align="right">{1013}</TableCell>
                                    <TableCell align="right">1231231</TableCell>
                                    <TableCell component="th" scope="row">
                                        Red frog
                                    </TableCell>
                                    <TableCell align="right">false</TableCell>
                                    <TableCell align="right">123</TableCell>
                                    <TableCell align="right">dqwe</TableCell>
                                    <TableCell align="right">abd</TableCell>
                                </TableRow>
                        </TableBody>
                    </Table>
                </Paper>

                <div style={{ height: 30 }} />

                <Paper>
                    <Table>
                        <TableHead>
                            <TableRow>
                                <TableCell align="right">№ очереди</TableCell>
                                <TableCell align="right">Табель</TableCell>
                                <TableCell align="right">ФИО</TableCell>
                                <TableCell align="right">Родитель одиночка</TableCell>
                                <TableCell align="right">Категория</TableCell>
                                <TableCell align="right">Корпоративные награды (последние 2 года)</TableCell>
                            </TableRow>
                        </TableHead>
                        <TableBody>
                            {rows.map((row, index) => (
                                <TableRow key={row.id}>
                                    <TableCell align="right">{index + 1000}</TableCell>
                                    <TableCell align="right">{index * 5132 + 1213}</TableCell>
                                    <TableCell component="th" scope="row">
                                        {row.name}
                                    </TableCell>
                                    <TableCell align="right">{row.calories}</TableCell>
                                    <TableCell align="right">{row.fat}</TableCell>
                                    <TableCell align="right">{row.carbs}</TableCell>
                                    <TableCell align="right">{row.protein}</TableCell>
                                </TableRow>
                            ))}
                        </TableBody>
                    </Table>
                </Paper>
            </div>);
    }
}

export default withStyles(styles)(Queue);