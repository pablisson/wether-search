import axios from 'axios';
import cors from 'cors';

const apiAxios = axios.create({
  baseURL: 'http://localhost:8000/',
});

export const api = {
  enviaCidade: async (region) => {
    try {
      console.log('region:', region);
      const data = await apiAxios.post('weather/',{'name':region})
      console.log('data:', data);
      return data;
    } catch (error){
      console.log('Error:enviaCidade:', JSON.stringify(error.message))
      return false
    }
  },
  


}