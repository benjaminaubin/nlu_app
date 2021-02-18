import React, { FunctionComponent } from 'react';
import { View, Text} from 'react-native';
import NLU from './components/NLU';


const App: FunctionComponent<{}> = () => {
  return (
      <>
      <View style={styles.container}>
        <Text style={styles.title}>Natural Language Understanding</Text>
        <Text style={styles.subtitle}>Application in ReactNative, Typescript</Text>
        <NLU />
      </View>
      </>
  );
};

const styles = {
  container:{
    flex: 1,
    alignItems: 'center',
    backgroundColor: "#282c34",
  },
  title:{
    marginTop: 100,
    color: "#61dafb",
    fontSize:25,
    fontWeight: 'bold',
    marginBottom:30
  },
  subtitle:{
    color: "white",
    fontSize:20,
    fontWeight: 'bold',
    marginBottom:100
  }
}

export default App;
