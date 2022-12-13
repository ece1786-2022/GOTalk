import Button from 'react-bootstrap/Button';
import Stack from 'react-bootstrap/Stack'
import {useNavigate} from "react-router-dom";
import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';
import { useState } from 'react';
import React from 'react'

const buttonStyle = {
    width: '100px'
}

const Options = React.forwardRef(({handleOptions, loading}, ref)=>{
    const navigate = useNavigate()
    const [flag, setFlag] = useState(false)
    const OptionGroup = () =>{
      if(!flag){
        return(
          <Stack direction="horizontal" gap={3}>
            <Button key='A' disabled={loading} style={buttonStyle} size='lg' variant="light" 
            onClick={()=>handleOptions('A')}>A</Button>
            <Button key='B' disabled={loading} style={buttonStyle} size='lg'variant="light" 
            onClick={()=>handleOptions('B')}>B</Button>
            <Button key='C' disabled={loading} style={buttonStyle} size='lg' variant="light" 
            onClick={()=>handleOptions('C')}>C</Button>
            <Button key='D' disabled={loading} style={buttonStyle} size='lg' variant="light" 
            onClick={()=>{setFlag(true)}}>Other</Button>
        </Stack>
        )
      }else{
      return (
        <InputGroup style={{width:'40vw'}}>
            <Form.Control
              placeholder="Your reponse..."
              aria-label="Recipient's username with two button addons"
              ref={ref}
            />
            <Button size='lg' disabled={loading} variant="outline-light"
            onClick={()=>{handleOptions('D');setFlag(false)}}>Confirm</Button>
            <Button size='lg' disabled={loading} variant="outline-light" 
            onClick={()=>{setFlag(false)}}>Back</Button>
        </InputGroup>
          )
      }
    }
  return (
    <div className='options'>
        <OptionGroup/>
        <Button style={buttonStyle} size='lg' variant="danger" onClick={()=>navigate('/')}>Exit</Button>
    </div>
  );
}
)

export default Options
