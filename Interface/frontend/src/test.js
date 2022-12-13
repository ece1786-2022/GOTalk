function NewlineText(props) {
    const text = props.text;
    const newText = text.split('\n').map(str => <p>{str}</p>);
    
    return newText;
  }
export default function Test({text}) {

    return (
        <div className="scroll-view">
            <NewlineText text={text}/>
        </div>
    );
}