/** @jsx React.DOM */

// Pardon my hipster. react jquery bootstrap html5 single page app
var Hello = React.createClass({
    componentDidMount: function() {
        $(".flat").spectrum({
            flat: true,
            showInput: true,
            change: this.handleChange
        });
    },
    getInitialState: function() {
        return {selectedColor: '#00FF00'};
    },
    handleChange: function(color) {
        this.setState({selectedColor: color.toHexString()});
        var rgb = color.toRgb();
        console.log(rgb);
        $.post("/set_color", {red: rgb.r, green: rgb.g, blue: rgb.b});
    },
    render: function() {
        var borderStyle = {
            'border-style': 'solid',
            'border-width': '10px',
            'border-color': this.state.selectedColor
        };
        var fontColor = {
            'background-color': this.state.selectedColor,
            'width': '193px',
            'height': '40px',
            'margin-top': '8px'
        };
        var margin = {
            'margin': '8px'
        };
        var classes = "";
        return (
            <div className={classes}
                style={borderStyle}>
                <h2 style={margin}>
                    Current Color
                    <br/>
                    {this.state.selectedColor}
                    <div style={fontColor}/>
                </h2>
                <br />
                <div style={margin}>
                    <input type="text" className="flat" value={this.state.selectedColor} />
                </div>
            </div>
        );
    }
});

var ColorPicker = React.createClass({
    render: function() {
        return (<Hello text="Wow" />);
    }
});

React.renderComponent(<ColorPicker />, document.getElementById('reactcontainer'));

