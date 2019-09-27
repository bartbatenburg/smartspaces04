import styled, {css} from 'styled-components';
import Tinct from 'tinct';
import PropTypes from "prop-types";

const Button = styled.div.attrs(props => {
	let hMargin = props.hMargin || props.margin || '10pt';
	let vMargin = props.vMargin || props.margin || '10pt';

	if (/[0-9]$/.test(hMargin)) hMargin += 'px';
	if (/[0-9]$/.test(vMargin)) vMargin += 'px';

	return ({
		height: '36px',
		width: props.width,
		hMargin,
		vMargin,
		padding: '10pt',
		bgColor: props.color,
		txtColor: props.textColor
	})
})`
	display: inline-block;
	box-sizing: border-box;
	height: ${props => props.height};
	width: calc(${props => props.width} - 2*${props => props.hMargin});
	vertical-align: middle;
	
	margin: ${props => props.vMargin} ${props => props.hMargin};
	padding: 0 ${props => props.padding};

	border-radius: 2px;
	box-shadow: 
		rgba(0, 0, 0, 0.14) 0px 2px 2px 0px, 
		rgba(0, 0, 0, 0.12) 0px 3px 1px -2px, 
		rgba(0, 0, 0, 0.2) 0px 1px 5px 0px;

	font-size: 14px;
	letter-spacing: 0.5px;
	line-height: ${props => props.height};
	color: ${props => props.txtColor};
	text-align: center;
	text-transform: uppercase;
	overflow: hidden;

	cursor: pointer;
	user-select: none;
	
	transition: 0.375s;

	&:hover{
		box-shadow: 
			rgba(0, 0, 0, 0.14) 0px 3px 3px 0px,
			rgba(0, 0, 0, 0.12) 0px 1px 7px 0px,
			rgba(0, 0, 0, 0.2) 0px 3px 1px -1px;
	}
	
	background-color:${props => props.bgColor};
	
	${props => props.disabled && css`
		background-color: ${Tinct.lightGrey};
		color: ${Tinct.darkGrey};
		cursor: default;
		box-shadow: none;
		pointer-events: none;
	`}
`;

//TODO remove this thingy
Button.NoTopMargin = styled(Button)`
	margin-top: 0;
`;

Button.propTypes = {
	color: PropTypes.string,
	textColor: PropTypes.string,
	disabled: PropTypes.bool,
	margin: PropTypes.number,
	hMargin: PropTypes.number,
	vMargin: PropTypes.number,
};

Button.defaultProps = {
	color: Tinct.blue,
	textColor: Tinct.white,
	disabled: false,
	width: '100%'
};

export default Button