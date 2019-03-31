import * as React from "react";
import * as ReactDOM from "react-dom";
import TopBar from "./components/TopBar";

import Queue from "./containers/Queue";
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import HRQueue from "./containers/HRQueue";
import ApplicationPage from "./containers/ApplicationPage";

export class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = { showQueue: false, hrMode: false };
    }
    handleChange = (name) => () => event => {
        this.setState({ [name]: event.target.checked });
    };
    render() {
        let renderPage;
        if (this.state.showQueue) {
            renderPage = this.state.hrMode ? <HRQueue /> : <Queue />;
        } else {
            renderPage = <ApplicationPage />
        }

        return (
            <div>
                <TopBar
                    showQueue={this.state.showQueue}
                    hrMode={this.state.hrMode}
                    showQueueChanged={this.handleChange('showQueue')}
                    hrModeChanged={this.handleChange('hrMode')}
                />

                <Grid container spacing={24}>
                    <Grid item xs={12}>
                        {renderPage}
                    </Grid>
                </Grid>
            </div>
        );
    }
}