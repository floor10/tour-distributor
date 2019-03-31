import * as React from "react";
import * as ReactDOM from "react-dom";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Switch from '@material-ui/core/Switch';
import FormControlLabel from '@material-ui/core/FormControlLabel';

// const styles = theme => ({appBarSpacer: theme.mixins.toolbar});

export default (props => (
    <div>
        <AppBar>
            <Toolbar>
                <FormControlLabel
                    control={
                        <Switch
                            checked={props.showQueue}
                            onChange={props.showQueueChanged()}
                            value="showQueue"
                        />
                    }
                    label="Application page"
                />
                <FormControlLabel
                    control={
                        <Switch
                            checked={props.hrMode}
                            onChange={props.hrModeChanged()}
                            value="showQueue"
                        />
                    }
                    label="HR mode"
                />
            </Toolbar>
        </AppBar>
        <div style={{height: 70}} />
    </div>

));

