import { useState, useEffect } from "react";
import { Item } from "./Item"
import styles from './Content.module.css'
import { api } from "../services/api";
import { InputRegion } from "./InputRegion";
import { ButtonSendRegion } from "./ButtonSendRegion";
import { Checkbox } from "./CheckboxRegion"

export function Content(){
  const [region, setRegion] = useState('');
  const [list, setList] = useState([]);
  const [listAux, setListAux] = useState([]);
  const [checked, setChecked] = useState(false);


  const handleChange = () => {
    setChecked(!checked);
  };
  


  function onChangeRegion(region){    
    setRegion(region);
  }

  const handleSearchBD = async () => {
    //useEffect(() => {
      setListAux(list.map((item, index) => 
        console.log('lista', item.dt)

  
    ));
  //}, [list])
    //const {data} = await api.getWeather(region,checked);
    //console.log('list:', list);
    //setList(data);    
  }

  const handleSearch = async () => {
    const {data} = await api.getWeather(region,checked);
    console.log('data:', data);
    setList(data);    
  }

  function getStyle(value){
    switch (value) {
      case 0:
        return styles.item1;
      case 1:
        return styles.item2;        
      case 2:
        return styles.item3;
      case 3:
        return styles.item4;
      case 4:
        return styles.item5;
      case 5:
        return styles.item6
    }
  }

  useEffect(() => {
    //console.log('list: ', list);
    setListAux(list.map((item, index) => 
    <div key={index} className={getStyle(index)}>
      <div className={styles.fundo}>
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
    </div>
    ))
  }, [list])



  


  return (  
    <div className={styles.content}>
      <div>
        <h3>Seja bem vindo</h3>
        <h1>Selecione uma Cidade</h1>
        <InputRegion onChangeRegion={event => onChangeRegion(event.target.value)} value={region}/>
        <ButtonSendRegion onClick={() => handleSearch(region)}  label="Enviar"/>   
        <Checkbox label="Buscar no Banco" value={checked} onChange={event => handleChange(event.target.value)} /> 

        <ButtonSendRegion onClick={() => handleSearchBD(region)}  label="Salvar no Banco"/>        
        
        
        <div className={styles.colunas}>
          {listAux}
        </div>        
      </div>
      <div>
      </div>

    </div>
  );
}