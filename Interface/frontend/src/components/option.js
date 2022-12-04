import Button from 'react-bootstrap/Button';
import Stack from 'react-bootstrap/Stack'
import {useNavigate} from "react-router-dom";

const buttonStyle = {
    width: '100px'
}

export default function Options() {
    const navigate = useNavigate()
  return (
    <div className='options'>
        <Stack direction="horizontal" gap={3}>
            <Button style={buttonStyle} size='lg' variant="primary">A</Button>
            <Button style={buttonStyle} size='lg'variant="primary">B</Button>
            <Button style={buttonStyle} size='lg' variant="primary">C</Button>
        </Stack>
        <Button style={buttonStyle} size='lg' variant="danger" onClick={()=>navigate('/')}>Exit</Button>
    </div>
  );
}
