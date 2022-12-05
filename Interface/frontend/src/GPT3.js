import ScrollView from './components/scrollView'
import Options from './components/option';
import Stack from 'react-bootstrap/Stack';
import LoadingView from './components/loading';
import {useLocation, Navigate} from 'react-router-dom';
import {useState, useEffect, useRef, createRef} from 'react';

function GPT3() {
  const location = useLocation()
  const [option, setOption] = useState('')
  const [count, setCount] = useState(1)
  const [text, setText] = useState('')
  const [loading, setLoading] = useState(true)
  const [options, setOptions] = useState({})
  const [refresh, setRefresh] = useState(true)
  const otherRef = useRef()
  const scrollViewRef = useRef()

  useEffect(()=>{
    setLoading(true)
    generateContext()
    scrollToBottom()
  }, [count])

  useEffect(()=>{
    scrollToBottom()
  },[refresh])

  const scrollToBottom = () => {
    scrollViewRef.current?.scrollBy({ top: 500, behavior: "smooth" })
  }
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
        setLoading(false)
        setOptions(res.options)
        setRefresh(!refresh)
        }
      )
    }; 
  
  const handleOptions = (e) =>{
    if(e ==='D'){
      console.log(otherRef.current.value)
      setText(text + `\nOption selected: D. Other: ${otherRef.current.value}\n`)
    }else{
      setText(text + `\nOption selected: ${options[e]}\n`)
    }
    setOption(e)
    setCount(count+1)
  }

  if (!location.state || !location.state.key){
    return <Navigate to="/" state={{ from: location }} replace/>;
  }
  return (
    <div className='App'>
      {loading?<LoadingView/>:<></>}
      <Stack direction="vertical" gap={3}>
       <ScrollView ref={scrollViewRef} text={text}/>
        <Options handleOptions={handleOptions} loading={loading} ref={otherRef}/>
      </Stack>
    </div>
  );
}

export default GPT3;
