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
    const [ending, setEnding] = useState(1)
    const [round, setRound] = useState(10)

    // clear key 
    useEffect(()=>{
        setEnding('1')
        setKey(null)
    },[])

    const onFormSubmit = e => {
        e.preventDefault()
        navigate('/GPT3',{state:{key:apiKey, ending:ending, round: round}})
      }

    const popover = (
        <Popover id="popover-basic">
          <Popover.Body>
              <Form onSubmit={onFormSubmit}>
                  <Form.Group name="key" className="mb-3">
                    <Form.Label>OpenAI key</Form.Label>
                    <Form.Control type="password" placeholder="Password" onChange={(e)=>setKey(e.target.value)} />
                  </Form.Group>
                  <Form.Group name="ending">
                    <Form.Label>Select ending</Form.Label>
                  <Form.Select aria-label="Default select example" onChange={e => {setEnding(e.target.value)}}>
                    <option value="1">Jon Snow becomes the King</option>
                    <option value="2">Jon Snow kills the nightking</option>
                    <option value="3">Jon snow finds his love of the life</option>
                    </Form.Select>
                  </Form.Group>
                  <Form.Group name="round">
                    <Form.Label>Select round</Form.Label>
                  <Form.Select aria-label="Default select example" onChange={e => {setRound(e.target.value)}}>
                    <option value="5">5</option>
                    <option value="10">10</option>
                    <option value="15">15</option>
                    </Form.Select>
                  </Form.Group>
                  <Button style={{marginTop:'5px'}} variant="dark" type="submit">
                  Start
                 </Button>
              </Form>
          </Popover.Body>
        </Popover>
      );
      
    return (
        <div className="Home">
            <div className="center-box">
            <Button disabled={true} sytle={buttonStyle} size='lg' variant="outline-light" onClick={()=>{navigate('/GPT2',{state:{key:1}})}}>
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