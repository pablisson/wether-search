// props: 
export function Item(props){
    return (
        <div>
            
            <p>{props.dt_txt}</p>
            <p>{props.dt_txt}</p>
            <p>{props.temp}</p>
            <p>{props.feels_like}</p>
            <p>{props.temp_min}</p>
            <p>{props.temp_max}</p>
            <p>{props.pressure}</p>
            <p>{props.sea_level}</p>
            <p>{props.grnd_level}</p>
            <p>{props.humidity}</p>
            <p>{props.description}</p>
            <p><img src={`http://openweathermap.org/img/wn/${props.icon}@2x.png`}/></p>
            <p>{props.all}</p>
            <p>{props.speed}</p>
            <p>{props.deg}</p>
            <p>{props.gust}</p>

            
        </div>
    );
}

/*
            <p>{props.dt_txt}</p>
            <p>{props.dt_txt}</p>
            <p>{props.temp}</p>
            <p>{props.feels_like}</p>
            <p>{props.temp_min}</p>
            <p>{props.temp_max}</p>
            <p>{props.pressure}</p>
            <p>{props.sea_level}</p>
            <p>{props.grnd_level}</p>
            <p>{props.humidity}</p>
            <p>{props.temp_kf}</p>

        //weather
            <p>{props.id}</p>
            <p>{props.main}</p>
            <p>{props.description}</p>
            <p>{props.icon}</p>

        //clouds
            <p>{props.all}</p>

        //wind
            <p>{props.speed}</p>
            <p>{props.deg}</p>
            <p>{props.gust}</p>
*/