import * as React from "react";
import * as ReactDOM from "react-dom";
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Switch from '@material-ui/core/Switch';
import FormControlLabel from '@material-ui/core/FormControlLabel';

export const TopBar = props => (
    <AppBar>
        <Toolbar>
            <FormControlLabel
                control={
                    <Switch
                        checked={props.showQueue}
                        onChange={props.handleShowQueueChange()}
                        value="showQueue"
                    />
                }
                label="Secondary"
            />
        </Toolbar>
    </AppBar>
);

