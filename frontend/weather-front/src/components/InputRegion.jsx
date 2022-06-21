export function InputRegion(props){
    return (
        <div>
            <input type="text" onChange={props.onChangeRegion} value={props.value}/>
        </div>
    );
}