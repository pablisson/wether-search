import { useState, useEffect } from 'react';
import styles from './Item.module.css';



export function Item(props){
  const [day, setDay] = useState('');

  function getDay(date) {
    const d = new Date(date);
    let dayOfWeek = d.getDay();
    
    switch (new Date(date).getDay()) {
      case 0:
        setDay("SUN");
        break;
      case 1:
        setDay("MON");
        break;
      case 2:
        setDay("TUE");
        break;
      case 3:
        setDay("WED");
        break;
      case 4:
        setDay("THU");
        break;
      case 5:
        setDay("FRI");
        break;
      case 6:
        setDay("SAT");
        break;
    }

  };

  useEffect(() => {
    getDay(props.dt_txt)
  }, [])
  

  return (
      <div className={styles.propweather}>            
          <div className={styles.topweather}>
            <img className={styles.imgtype} src={`http://openweathermap.org/img/wn/${props.icon}@2x.png`}/>
            <span >{day}</span>
          </div>
          <h3 className={styles.temp}>{props.temp}º</h3>
          <p>{props.speed} m/s</p>       
          <p>{props.humidity} %</p>
          <p>{props.description}</p>
      </div>
  );
}