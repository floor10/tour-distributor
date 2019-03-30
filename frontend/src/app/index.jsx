import * as React from "react";
import * as ReactDOM from "react-dom";
import { TopBar } from "./components/TopBar";

import { Queue } from "./containers/Queue";
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

export class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = { showQueue: true };
    }
    handleShowQueueChange = () => event => {
        this.setState({ showQueue: event.target.checked });
    };
    render() {
        let renderPage;
        if (this.state.showQueue) {
            renderPage = <Queue />
        } else {
            renderPage = <p>Oops, something goes wrong</p>;
        }

        return (
            <div>
                <TopBar showQueue={this.state.showQueue} handleShowQueueChange={this.handleShowQueueChange.bind(this)} />
                <Grid container spacing={24}>
                    <Grid item xs={12}>
                        {renderPage}
                    </Grid>
                </Grid>
            </div>
        );
    }
}