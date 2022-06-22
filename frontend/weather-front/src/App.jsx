import { Content } from "./components/ContentWeather";
import { Sidebar } from "./components/Sidebar";

import './styles/global.css'
import styles from './App.module.css'

export function App() {
  return (
    <>
      <div className={styles.container}>
        <div className={styles.content}>

            <Sidebar/>

            <Content/>


        </div>
      </div>
    </>
  );
}

export default App
