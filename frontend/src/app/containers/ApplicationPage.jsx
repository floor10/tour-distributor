import * as React from "react";
import * as ReactDOM from "react-dom";
import TextField from '@material-ui/core/TextField';
import FormGroup from '@material-ui/core/FormGroup';
import Stepper from '@material-ui/core/Stepper';
import Step from '@material-ui/core/Step';
import StepLabel from '@material-ui/core/StepLabel';
import StepContent from '@material-ui/core/StepContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import Select from '@material-ui/core/Select';
import TableId from "../components/ApplicatinPage/TableId";
import Type from "../components/ApplicatinPage/Type";
import FamilyMembers from "../components/ApplicatinPage/FamilyMembers";

function getSteps() {
    return ['Табельный номер', 'Тип заявки', 'Выбор членов семьи'];
}

function getStepContent(step) {
    switch (step) {
        case 0:
            return (<TableId />);
        case 1:
            return (<Type />);
        case 2:
            return (<FamilyMembers />);
        default:
            return 'Unknown step';
    }
}

export default class ApplicationPage extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            activeStep: 0,
        };
    }
    handleBack() {
        if (this.state.activeStep != 0)
            this.setState({ activeStep: this.state.activeStep - 1 })
    }
    handleNext() {
        if (this.state.activeStep + 1 != getSteps().length) {
            this.setState({ activeStep: this.state.activeStep + 1 })
        }
    }
    render() {
        const steps = getSteps();
        return (
            <div>
                <Stepper activeStep={this.state.activeStep} orientation="vertical">
                    {steps.map((label, index) => (
                        <Step key={label}>
                            <StepLabel>{label}</StepLabel>
                            <StepContent>
                                {getStepContent(index)}
                                <div>
                                    <div>
                                        <Button
                                            disabled={this.state.activeStep === 0}
                                            onClick={this.handleBack.bind(this)}

                                        >
                                            Back
                                        </Button>
                                        <Button
                                            variant="contained"
                                            color="primary"
                                            onClick={this.handleNext.bind(this)}

                                        >
                                            {this.state.activeStep === steps.length - 1 ? 'Finish' : 'Next'}
                                        </Button>
                                    </div>
                                </div>
                            </StepContent>
                        </Step>
                    ))}
                </Stepper>
            </div>);
    }
}