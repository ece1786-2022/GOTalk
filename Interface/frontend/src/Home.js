import {useNavigate, Navigate} from "react-router-dom";
import Button from 'react-bootstrap/Button'
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Popover from 'react-bootstrap/Popover';
import Form from 'react-bootstrap/Form';
import { useState, useEffect } from "react";


const buttonStyle = {
    width: '500px',
}
export default function Home(){
    const [apiKey, setKey] = useState()
    const navigate = useNavigate()

    // clear key 
    useEffect(()=>{
        setKey(null)
    },[])

    const onFormSubmit = e => {
        e.preventDefault()
        navigate('/GPT3',{state:{key:apiKey}})
      }

    const popover = (
        <Popover id="popover-basic">
          <Popover.Body>
              <Form onSubmit={onFormSubmit}>
                  <Form.Group name="key" className="mb-3">
                    <Form.Label>OpenAI key</Form.Label>
                    <Form.Control type="password" placeholder="Password" onChange={(e)=>setKey(e.target.value)} />
                  </Form.Group>
                  <Button variant="dark" type="submit">
                  Start
                 </Button>
              </Form>
          </Popover.Body>
        </Popover>
      );
      
    return (
        <div className="Home">
            <div className="center-box">
            <Button sytle={buttonStyle} size='lg' variant="outline-light" onClick={()=>{navigate('/GPT2',{state:{key:1}})}}>
                 <h1>GPT2</h1> 
            </Button>
            <OverlayTrigger trigger="click" placement="bottom" overlay={popover}>
                <Button sytle={buttonStyle} size='lg' variant="outline-light">
                    <h1>GPT3</h1> 
                </Button>
            </OverlayTrigger>
            </div>
        </div>
    )
}