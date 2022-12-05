import ProgressBar from 'react-bootstrap/ProgressBar';
import Spinner from 'react-bootstrap/Spinner';

function LoadingView() {
  return (
    <div className='loading-spinner'>
         <Spinner animation="border" variant="light" />
    </div>
  )
}

export default LoadingView;