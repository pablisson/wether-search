import styles from './ButtonSendRegion.module.css';

export function ButtonSendRegion(props){
    return (
        <div>
            <button onClick={props.onClick}>{props.label}</button>            
        </div>
    );
}