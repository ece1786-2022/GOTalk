import ScrollView from './components/scrollView'
import Options from './components/option';
import Stack from 'react-bootstrap/Stack';
import {useLocation, Navigate} from 'react-router-dom'

function GPT3() {
  const location = useLocation()
  if (!location.state || !location.state.key){
    return <Navigate to="/" state={{ from: location }} replace/>;
  }
  console.log(location.state.key)
  return (
    <div className='App'>
      <Stack direction="vertical" gap={3}>
        <ScrollView/>
        <Options/>
      </Stack>
    </div>
  );
}

export default GPT3;
