import { useState } from "react";
import { Item } from "./Item"
import styles from './Content.module.css'
import { api } from "../services/api";
import { InputRegion } from "./InputRegion";
import { ButtonSendRegion } from "./ButtonSendRegion";

export function Content(){
  const [region, setRegion] = useState('');

  const handleSearch = async () => {
    const aux = await api.enviaCidade(region);
    console.log('aux:', aux);
  }

  function onChangeRegion(region){    
    setRegion(region);
  }

  return (  
    <div className={styles.content}>
      <div>
        <h3>Seja bem vindo</h3>
        <h1>Selecione uma Cidade</h1>
        <InputRegion onChangeRegion={event => onChangeRegion(event.target.value)} value={region}/>
        <ButtonSendRegion onClick={() => handleSearch(region)}/>         

        <div className={styles.colunas}>
          <div className={styles.um}>
          <Item 
            dt = "1647345600"
            dt_txt="2022-03-15 12:00:00"
            
            temp="286.66"
            feels_like="285.22"
            temp_min="286.32"
            temp_max="286.66"
            pressure="1007"
            sea_level="1007"
            grnd_level="982"
            humidity="44"
            temp_kf="0.34"

          
            id="800"
            main="Clear"
            description="clear sky"
            icon="01n"

            
            all="0"

            
            speed="3.82"
            deg="84"
            gust="6.53"

            DiaSemana="" 
            Temperatura=""
            Vento=""
          />
          </div>
          <div className={styles.dois}>
          <Item 
            dt = "1647345600"
            dt_txt="2022-03-15 12:00:00"
            
            temp="286.66"
            feels_like="285.22"
            temp_min="286.32"
            temp_max="286.66"
            pressure="1007"
            sea_level="1007"
            grnd_level="982"
            humidity="44"
            temp_kf="0.34"

          
            id="800"
            main="Clear"
            description="clear sky"
            icon="01n"

            
            all="0"

            
            speed="3.82"
            deg="84"
            gust="6.53"

            DiaSemana="" 
            Temperatura=""
            Vento=""
          />
          </div>
          <div className={styles.tres}></div>
          <div className={styles.quatro}></div>
          <div className={styles.cinco}></div>
          <div className={styles.seis}></div>
          <div className={styles.sete}></div>

        </div>
        
      </div>
      <div>
      </div>

    </div>
  );
}