import { Content } from "./components/Content";
import { Sidebar } from "./components/Sidebar";

import './global.css'
import styles from './App.module.css'

export function App() {
  return (
    <div>
      
      <div className={styles.wrapper}>
        <aside>
          <Sidebar/>
        </aside>

        <main>
          <Content/>
        </main>

      </div>
    </div>
  );
}

export default App
