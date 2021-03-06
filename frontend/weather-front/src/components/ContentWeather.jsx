import { useState, useEffect } from "react";
import { Item } from "./Item";
import styles from './ContentWeather.module.css';
import { api } from "../services/api";
import { InputRegion } from "./InputRegion";
import { ButtonSendRegion } from "./ButtonSendRegion";
import { useInsertionEffect } from "react";

export function Content(){
  const [region, setRegion] = useState('');
  const [list, setList] = useState([]);
  const [listAux, setListAux] = useState([]);
  const [checked, setChecked] = useState(false);

  const [currentCity, setCurrentCity] = useState('');
  const [currentTemp, setCurrentTemp] = useState('');
  const [currentWind, setCurrentWind] = useState('');
  const [currentlat, setCurrentlat] = useState('');
  const [currentlon, setCurrentlon] = useState('');


  const handleChange = () => {
    setChecked(!checked);
  };

  function onChangeRegion(region){    
    setRegion(region);
  }

  const handleSearchBD = async () => {
    for(const item of list){
      //console.log('item',item)
      const jsonItem = {
          "dt_txt": item["dt_txt"].toString(),
          "temp" : item["temp"].toString(),
          "feels_like" : item["feels_like"].toString(),
          "temp_min" : item["temp_min"].toString(),
          "temp_max" : item["temp_max"].toString(),
          "pressure" : item["pressure"].toString(),
          "humidity" : item["humidity"].toString(),          
          "description" : item["description"].toString(),
          "icon" : item["icon"].toString(),
          "speed" : item["speed"].toString(),
          "deg" : item["deg"].toString(),
          "all" : item["all"].toString(),
          "dt" : item["dt"].toString(),
          "lat": item["lat"].toString(),
          "lon" : item["lon"].toString(),
          "city" : item["city"].toString(),
          "country": item["country"].toString(),
          

      };
      await api.postWeather(jsonItem)
      
      console.log(jsonItem);
    }


  };

  const handleSearch = async () => {
    const {data} = await api.getWeather(region,checked);
    console.log('data:', data);
    setList(data);    
    setCurrentCity(data[0].city);
    setCurrentTemp(data[0].temp);
    setCurrentlat(data[0].lat);
    setCurrentlon(data[0].lon);
  }

  useEffect(() => {
    console.log('list: ', list);
    setListAux(list.map((item, index) =>       
         
        <div className={styles.boxweather}>
          <Item             
            dt ={item.dt}
            dt_txt={item.dt_txt}      
            temp={item.temp}
            feels_like={item.feels_like}
            temp_min={item.temp_min}
            temp_max={item.temp_max}
            pressure={item.pressure}
            sea_level={item.sea_level}
            grnd_level={item.grnd_level}
            humidity={item.humidity}        
            description={item.description}
            icon={item.icon}      
            speed={item.speed}
            deg={item.deg}
            gust={item.gust}  
          />
        </div>      
    
    ))
  }, [list])



  return (  
    <div className={styles.container}>
      <h3>Seja bem vindo</h3>
      <h1>Selecione uma Cidade</h1>
      <div className={styles.colunas}>
        <InputRegion onChangeRegion={event => onChangeRegion(event.target.value)} value={region}/>
        <ButtonSendRegion onClick={() => handleSearch(region)}  label="Buscar Dados"/>           
        <ButtonSendRegion onClick={() => handleSearchBD()}  label="Salvar no Banco"/>        
      </div>
      {list?.length > 0 &&
      <div className={styles.content}>        
        <div>
          <div className={styles.boxcurrentweather}>
              
                
                <div className={styles.boxinline}>

                  <div>
                    <div>Cidade</div>
                    <div className={styles.h2}>
                      {currentCity}                
                    </div>
                  </div>

                  <div>
                    <div>Temperatura</div>
                    <div className={styles.h2}>
                      {currentTemp}??                
                    </div>
                  </div>

                  <div>
                    <div>Coordenadas</div>
                    <div className={styles.h2}>
                      [{currentlat} ,{currentlon} ]
                    </div>
                  </div>

                </div>
            
          </div>
          <div className={styles.colunas}>
            {listAux}            
          </div> 
        </div>       
      </div>
      }
    </div>



  );
}