import styles from './Sidebar.module.css'
import logoImg from '../assets/logo.png'

export function Sidebar(){
  return (  
    <div className={styles.sidebar}>
      <img src={logoImg} alt="linx" className={styles.img_logo}/>
    </div>
  );
}