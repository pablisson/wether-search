import axios from 'axios';
import cors from 'cors';

const apiAxios = axios.create({
  baseURL: 'http://localhost:8000/',
});

export const api = {
  postWeather: async (item) => {
    try {
      console.log('item:', item);
      
      const data = await apiAxios.post('weather/', item)
      console.log('data:', data);
      return data;
    } catch (error){
      console.log('Error:salvaWeather:', JSON.stringify(error.message))
      return false
    }
  },
  getWeather: async (city, isdb) => {
    try {      
      console.log(city, isdb)
      
      const data = await apiAxios.get(`weather/?nome=${city}&db=${isdb}`)
      //console.log('data:', data);
      return data;
    } catch (error){
      console.log('Error:getWeather:', JSON.stringify(error.message))
      return false
    }
  },
  


}