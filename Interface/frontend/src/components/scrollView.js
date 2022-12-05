import React from 'react'


function NewlineText(props) {
  const text = props.text;
  const newText = text.split('\n').map(str => <p style={{color:'white'}}>{str}</p>);
  return newText;
}

const background = "Jon Snow was standing in the courtyard of the Red Keep, surrounded by the noise and commotion of a bustling castle."+
    " The sun was setting, casting a pinkish hue across the stone walls and cobbled pathways. "+
    "Jon had just been told that he was going to take part in a special mission for the Lord Commander of the Night's Watch, and he was apprehensive. \n \n\n"+
    "Dialogue Options: \nA. I'm ready for whatever task is ahead of me"+
    "\nB. I'm nervous about this mission \nC. What can I do to help? \nD. Other \nOption selected:  A. I'm ready for whatever task is ahead of me\n"

const ScrollView = React.forwardRef((props,ref)=>{

    return (
        <div className="scroll-view" ref={ref}>
            <NewlineText text={background}/>
            <NewlineText text={props.text}/>
        </div>
    );
}
)

export default ScrollView