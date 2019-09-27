import React from 'react';
import styled from 'styled-components';

const Wrapper = styled.div`
	display: flex;
	position: absolute;
	justify-content: center;
	align-items: center;
	height: 100%;
	width: 100%;
`;

const Inner=styled.div.attrs(({width, height})=>{
	return {width, height};
})`
	width: ${props=>props.width};
	height: ${props=>props.height};
	position: relative;
`;

const Center = ({width, height, children, ...props}) => {
	width = width ? width : 'auto';
	height = height ? height : 'auto';

	return (
		<Wrapper {...props}>
			<Inner width={width} height={height}>
				{children}
			</Inner>
		</Wrapper>
	);
};

export default Center;