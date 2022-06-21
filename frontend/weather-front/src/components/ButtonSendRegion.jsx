export function ButtonSendRegion(props){
    return (
        <div>
            <button onClick={props.onClick}>{props.label}</button>            
        </div>
    );
}