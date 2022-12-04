import ScrollView from './components/scrollView'
import Options from './components/option';
import Stack from 'react-bootstrap/Stack';
import {useLocation, Navigate} from 'react-router-dom';
import {useState, useEffect} from 'react';

function GPT3() {
  const location = useLocation()
  const [option, setOption] = useState('')
  const [count, setCount] = useState(0)
  const [text, setText] = useState('')
  useEffect(()=>{
    generateContext()
  }, [option])
  const generateContext = () =>{
    const requestBody = {
        method: "POST",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          key:location.state.key,
          count,
          option, 
          ending: location.state.ending,
          round: location.state.round,
          context: text
        })
    };

    fetch("http://localhost:5000/api/GPT3", requestBody)
    .then((res)=>{
      return res.json()
    })
    .then((res)=>{
        console.log(res.text)
        setText(text + res.text)
        }
      )
    }; 
  
  const handleOptions = (e) =>{
    setCount(count+1)
    setOption(e)
  }

  if (!location.state || !location.state.key){
    return <Navigate to="/" state={{ from: location }} replace/>;
  }
  return (
    <div className='App'>
      <Stack direction="vertical" gap={3}>
        <ScrollView text={text}/>
        <Options handleOptions={handleOptions}/>
      </Stack>
    </div>
  );
}

export default GPT3;
